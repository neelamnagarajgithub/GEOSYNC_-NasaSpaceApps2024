import { Module } from '@nestjs/common';
import { MetadataService } from './metadata.service';
import { MetadataController } from './metadata.controller';
import { HttpModule, HttpService } from '@nestjs/axios';

@Module({
  imports:[HttpModule],
  providers: [MetadataService],
  controllers: [MetadataController]
})
export class MetadataModule {}
