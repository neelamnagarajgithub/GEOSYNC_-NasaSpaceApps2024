import express from 'express';
import vindices from '../controllers/Vindices.controller.js';

const vindices_router=express.Router();

vindices_router.post('/vindices',vindices);

export default vindices_router;