import { Injectable, HttpException, HttpStatus } from '@nestjs/common';
import { HttpService } from '@nestjs/axios';
import { catchError, map } from 'rxjs/operators';
import { Observable, throwError } from 'rxjs';
import * as https from 'https';
import { InternalAxiosRequestConfig } from 'axios';
import { response } from 'express';

@Injectable()
export class MetadataService {
   apikey: string;
  constructor(private readonly httpService: HttpService) {
    this.httpService.axiosRef.interceptors.request.use((config: InternalAxiosRequestConfig) => {
      if (this.apikey) {
        config.headers['X-Auth-Token'] = this.apikey;
      }
      return config;
    });
  }


  async loginwithtoken(): Promise<any> {
    const loginurl = 'https://m2m.cr.usgs.gov/api/api/json/stable/login-token';
    
    // Create an HTTPS agent that ignores SSL certificate errors
    const httpsAgent = new https.Agent({
      rejectUnauthorized: false,
    });

    const response = await  this.httpService.post(loginurl, {
      username: "neelamnagaraj99@gmail.com",
      token:"mTkwF56sLZAIC6mGQ4prlGiZmFzEJb5NL7uvH9JGfwO7z3HuP_ZfuYagARgxFU!f"
    }, {
      httpsAgent: httpsAgent,
    }
    )
    .pipe(
      map(response => response.data),
      catchError((error) => {
        // Log detailed error information
        console.error('Error occurred:', {
          message: error.message,
          response: error.response?.data,
          status: error.response?.status,
          headers: error.response?.headers,
        });
         throw new HttpException({
          status: HttpStatus.INTERNAL_SERVER_ERROR,
          error: 'An error occurred while logging in',
        }, HttpStatus.INTERNAL_SERVER_ERROR);
      })
    ).toPromise();
    this.apikey=response.data;
    return response;
  }

  async searchScenes(wrsPath: string, wrsRow: string): Promise<any> {
    const searchUrl = 'https://m2m.cr.usgs.gov/api/api/json/stable/scene-search';
    
    const response = await this.httpService.post(searchUrl, {
      datasetName: 'landsat_ot_c2_l2',
      sceneFilter:{ additionalCriteria: {
        filterType: 'and',
        childFilters: [
          {
            filterType: 'value',
            fieldId: '5e83d15051254e26', // WRS Path field ID
            value: wrsPath
          },
          {
            filterType: 'value',
            fieldId:  '5e83d14ff1eda1b8', // WRS Row field ID
            value: wrsRow
          }
        ]
      },
      metadataType: "full"
    }
    }, {
      headers: {
        'X-Auth-Token': 'eyJjaWQiOjI3Mjc5OTY3LCJzIjoiMTcyNzUwMTMxNCIsInIiOjQ0MCwicCI6WyJ1c2VyIiwiZG93bmxvYWQiLCJvcmRlciJdfQ==',
      },
      httpsAgent: new https.Agent({
        rejectUnauthorized: false,
      }),
    })
    .pipe(
      map(response => response.data),
      catchError((error) => {
        // Log detailed error information
        console.error('Error occurred:', {
          message: error.message,
          response: error.response?.data,
          status: error.response?.status,
          headers: error.response?.headers,
        });
        throw new HttpException({
          status: HttpStatus.INTERNAL_SERVER_ERROR,
          error: 'An error occurred while searching for scenes',
        }, HttpStatus.INTERNAL_SERVER_ERROR);
      })
    ).toPromise();

    return response;
  }

  async getSceneMetadata(): Promise<any> {
    const metadataUrl = 'https://m2m.cr.usgs.gov/api/api/json/stable/scene-metadata';
    
    const response = await this.httpService.post(metadataUrl, {
      datasetName: 'landsat_ot_c2_l2',
      entityId:" LC90090082024268LGN00"
    }, {
      headers: {
        'X-Auth-Token':  'eyJjaWQiOjI3Mjc5OTY3LCJzIjoiMTcyNzUwMTMxNCIsInIiOjQ0MCwicCI6WyJ1c2VyIiwiZG93bmxvYWQiLCJvcmRlciJdfQ==',
      },
      httpsAgent: new https.Agent({
        rejectUnauthorized: false,
      }),
    })
    .pipe(
      map(response => {
        const data = response.data.data;
        return {
            acquisitionDate: data.metadata.find(item => item.fieldName === 'Date Acquired')?.value,
            satellite: data.metadata.find(item => item.fieldName === 'Satellite')?.value,
            startTime: data.metadata.find(item => item.fieldName === 'Start Time')?.value,
            stopTime: data.metadata.find(item => item.fieldName === 'Stop Time')?.value,
            latitude: data.metadata.find(item => item.fieldName === 'Scene Center Latitude')?.value,
            longitude: data.metadata.find(item => item.fieldName === 'Scene Center Longitude')?.value,
            wrsPath: data.metadata.find(item => item.fieldName === 'WRS Path')?.value.trim(),
            wrsRow: data.metadata.find(item => item.fieldName === 'WRS Row')?.value.trim(),
            cloudCover: data.cloudCover,
            imageQuality: data.metadata.find(item => item.fieldName === 'Image Quality')?.value
        };
    }),
      catchError((error) => {
        // Log detailed error information
        console.error('Error occurred:', {
          message: error.message,
          response: error.response?.data,
          status: error.response?.status,
          headers: error.response?.headers,
        });
        throw new HttpException({
          status: HttpStatus.INTERNAL_SERVER_ERROR,
          error: 'An error occurred while getting scene metadata',
        }, HttpStatus.INTERNAL_SERVER_ERROR);
      })
    ).toPromise();

    return response;
  }

  async getMetadataForScene(path: string, row: string): Promise<any> {
    const scenes = await this.searchScenes(path, row);
    if (!scenes||scenes.length === 0) {
      throw new HttpException({
        status: HttpStatus.NOT_FOUND,
        error: 'No scenes found for the given path and row',
      }, HttpStatus.NOT_FOUND);
    }

    const entityId = scenes[0].entityId;
    return this.getSceneMetadata( );
  }

}