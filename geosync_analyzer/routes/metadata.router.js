import express from 'express';
import metadata_lat from '../controllers/metadata.controller.js';

const metadata_router=express.Router();

metadata_router.get('/metadata',metadata_lat);

export default metadata_router