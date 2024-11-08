import { Body, Controller, Param, Post } from '@nestjs/common';
import { MetadataService } from './metadata.service';

@Controller('metadata')
export class MetadataController {
    constructor(private readonly metadataService: MetadataService) {}

    @Post('loginwithtoken')
    async loginwithtoken() {
        return this.metadataService.loginwithtoken();
    }

    @Post('getdata')
    async getmetadata() {
        return this.metadataService.getSceneMetadata( );
    }

    @Post('searchscenes')
    async searchScenes( ) {
        return this.metadataService.searchScenes('009','007');
    }
}
