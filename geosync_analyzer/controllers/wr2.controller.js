import {spawn} from 'child_process';


const wrs2_convo = async (req,res)=>{
    const latitude = req.query.latitude;
    const longitude = req.query.longitude;

    const pythonProcess = spawn('python3', ['py files/wrs2_coversion.py', latitude, longitude]);

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
                // Convert the result to a string and parse it
                const parsedResult = JSON.parse(result.trim());
                res.status(200).json(parsedResult);
            } catch (error) {
                res.status(500).send('Error parsing response from Python script');
            }
        }
    });
};

export default wrs2_convo;