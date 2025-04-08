//import express from express
//import cors from "cors";

//const app = express()

//app.use(express.json())
//app.use(cors())
//app.use("/", userRoutes)

//app.listen(8800);

import express from 'express';
import cors from 'cors';

const app = express();
app.use(cors());

app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});



