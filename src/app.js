import express from "express";
import dotenv from 'dotenv'
import { router } from "./routes/general.js";
dotenv.config()

const app = express();

app.use('/general', router)

app.get('/', (req, res) => {
  res.send('Hello, World!');
});


const port = 3000;

// Start the server and listen on the defined port
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});


