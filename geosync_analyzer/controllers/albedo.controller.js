import { spawn } from 'child_process';

const albedo = (req, res) => {
    const latitude = req.query.latitude;
    const longitude = req.query.longitude;

    const pythonProcess = spawn('python3', ['py files/albedo.py', latitude, longitude]);

    let base64Image = '';

    pythonProcess.stdout.on('data', (data) => {
        base64Image += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
        if (!res.headersSent) {
            res.status(500).send(data.toString());
        }
    });

    pythonProcess.on('close', (code) => {
        if (!res.headersSent) {
            try {
                res.json({ image: base64Image.trim() });
            } catch (error) {
                console.error(`Error parsing response from Python script: ${error}`);
                res.status(500).send('Error parsing response from Python script');
            }
        }
    });
};

export default albedo;