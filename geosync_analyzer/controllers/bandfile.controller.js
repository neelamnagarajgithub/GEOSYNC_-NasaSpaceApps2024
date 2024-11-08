import {spawn} from 'child_process';


const bandvalues = async (req,res)=>{
    const latitude = req.query.latitude;
    const longitude = req.query.longitude;

    const pythonProcess = spawn('python3', ['py files/earth_engine.py', latitude, longitude]);

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
                const wavelengths = [0.443, 0.483, 0.563, 0.655, 0.865, 1.610, 2.200];

                const wavelengthsDict = {};
                wavelengths.forEach((wavelength, index) => {
                    wavelengthsDict[`SR_B${index + 1}_Wavelength`] = wavelength;
                });

                parsedResult.wavelengths = wavelengthsDict;

                res.status(200).json(parsedResult);
            } catch (error) {
                console.error(`Error parsing response from Python script: ${error}`);
                res.status(500).send('Error parsing response from Python script');
            }
        }
    });
};

export default bandvalues;