import { selectAllPlayers, testSelect } from "../models/general.js";

export async function testMethod(req, res) {
    try {
        const result = await testSelect();
        return res.status(200).json(result)
    } catch (err) {
        return res.status(400).json({message: err});
    }

}


export async function getAllPlayers(req, res) {
    try { 
        console.log('got here')
        const result = await selectAllPlayers();
        return res.status(200).json(result);
    } catch (err) {
        return res.status(400).json({message: err});
    }
}