import express  from "express";
import { testMethod } from "../controllers/general.js";

export const router = express.Router()


router.get('/test-route', testMethod);