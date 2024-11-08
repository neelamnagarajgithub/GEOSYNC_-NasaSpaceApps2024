import express from 'express';
import albedo from '../controllers/albedo.controller.js';

const albedo_router=express.Router();

albedo_router.get('/albedo',albedo);

export default albedo_router;