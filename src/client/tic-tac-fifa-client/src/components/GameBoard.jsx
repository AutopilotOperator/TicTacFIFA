import { Grid } from "@mui/material"
import GridItem from "./GridItem"
import { useState } from "react";
import SideGridItem from "./SideGridItem";


const rowDivStyle = {
    display: 'flex',
    flexDirection: 'row',
    width: '50vw'
}

export default function GameBoard() {

    const [fieldConfig, setFieldConfig] = useState({
        rows: ['1', '2', '3'],
        columns: ['4', '5', '6']
    })

    const generateBoardItems = () => {
        const rowArr = [];
        let columnArr = [];
        columnArr.push(<div>Fifa Grid</div>)
        for (let i = 0; i < 3; i++) {
            columnArr.push(<SideGridItem key={i} value={fieldConfig.columns[i]}/>)
        }
        rowArr.push(<div key={'row-headers'} style={rowDivStyle}>{columnArr}</div>)
        for (let i = 0; i < 3; i++) {
            columnArr = [];
            columnArr.push(<SideGridItem key={'1-' + i} value={fieldConfig.rows[i]}/>)
            for (let j = 1; j < 4; j++) {
                columnArr.push(<GridItem row={i} column={j}/>)
            }
            rowArr.push(<div key={'row-' + i} style={rowDivStyle}>{columnArr}</div>)
        }
        return rowArr;
    }

    return (
        <div style={{
            backgroundColor: 'rgb(150, 150, 150)'
        }}>
            {generateBoardItems()}
        </div>
    )
}