import { open } from "sqlite";
import sqlite3 from "sqlite3";


export async function testSelect() {
    try {
        const db = await open({
            filename: './src/models/fifa.db',
            driver: sqlite3.Database
        })
        console.log(db)
        const result = await db.all("Select * from FIFA where overall = '90' and player_positions='GK' and fifa_update='9'");
        // const result = await db.all("SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name");
        console.log(result)
        await db.close()
        return result

    } catch (err) {
        console.log(err)
        throw err;
    }
}

