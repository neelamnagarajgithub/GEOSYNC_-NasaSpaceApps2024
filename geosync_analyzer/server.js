import express from "express";
import cors from "cors";
import morgan from "morgan";
import mongoose from "mongoose";
import dotenv from "dotenv";
import wrs2_router from './routes/wrs2.route.js';
import band_router from "./routes/bandfile.router.js";
import metadata_router from "./routes/metadata.router.js";
import vindices_router from "./routes/Vindices.route.js";
import albedo_router from "./routes/albedo.route.js";
const app = express();

dotenv.config({ path: "./config.env" });

app.use(express.json());
app.use(morgan('dev'))

app.use(cors({
  origin:["http://localhost:3000","https://geosync-ruby.vercel.app","https://geosync-ruby.vercel.app/map"],
  methods:['GET','POST'],
  credentials:true,
}))


const DB = process.env.DATABASE.replace(
  "<password>",
  process.env.DATABASE_PASSWORD
);

mongoose
  .connect(DB)
  .then(() => {
    console.log("Connected To MongoDB");
  })
  .catch((err) => {
    console.log(err);
  });

app.use('/api',wrs2_router)
app.use('/api',band_router)
app.use('/api',metadata_router)
app.use('/api',vindices_router)
app.use('/api',albedo_router)

const port = process.env.PORT || 11000;

app.listen(port, () => {
  console.log(`Server is Running on port ${port}`);
});