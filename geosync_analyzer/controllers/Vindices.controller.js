import {spawn} from 'child_process';


const vindices = async (req,res)=>{
    const band1=req.body.SR_B2
    const band2=req.body.SR_B3
    const band3=req.body.SR_B4
    const band4=req.body.SR_B5
    const band5=req.body.SR_B6
    const band4a=req.body.SR_B4

    console.log(band1,band2,band3,band4,band5,band4a)
    if (!band1 || !band2 || !band3 || !band4 || !band5 || !band4a) {
        return res.status(400).json({ error: 'All band values (SR_B2, SR_B3, SR_B4, SR_B5, SR_B6, SR_B4) are required' });
    }

    const pythonProcess = spawn('python3', ['py files/v_Indices.py', band1,band2,band3,band4,band5,band4a]);

    let result="";
    pythonProcess.stdout.on('data', (data) => {
       result += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
        res.status(500).send(data.toString());
    });

    pythonProcess.on('close', (code) => {
        if (!res.headersSent) {
            try {

                const parsedResult = JSON.parse(result.trim());
                res.status(200).json(parsedResult);
            } catch (error) {
                res.status(500).send('Error parsing response from Python script');
            }
        }
    });
};

export default vindices