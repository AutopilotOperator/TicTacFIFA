import express  from "express";
import { testMethod, getAllPlayers } from "../controllers/general.js";

export const router = express.Router()


router.get('/test-route', testMethod);

router.get('/all-players', getAllPlayers);