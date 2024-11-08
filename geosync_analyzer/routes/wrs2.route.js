import express from 'express';
import wrs2_convo from '../controllers/wr2.controller.js';

const wrs2_router=express.Router();

wrs2_router.get('/wrs2_coversation',wrs2_convo);

export default wrs2_router