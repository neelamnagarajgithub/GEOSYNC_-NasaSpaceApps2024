import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { UserModule } from './user/user.module';
import { PrismaModule } from './prisma/prisma.module';
import { MetadataModule } from './metadata/metadata.module';

@Module({
  imports: [UserModule, PrismaModule, MetadataModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
