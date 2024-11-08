import express from 'express';
import bandvalues from '../controllers/bandfile.controller.js';

const band_router=express.Router();

band_router.get('/spectralsign',bandvalues);

export default band_router