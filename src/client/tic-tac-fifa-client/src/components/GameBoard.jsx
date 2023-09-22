import { Grid } from "@mui/material"
import GridItem from "./GridItem"
import { useState } from "react";
import SideGridItem from "./SideGridItem";


const rowDivStyle = {
    display: 'flex',
    flexDirection: 'row',
    width: 'fit-content'
}

export default function GameBoard() {

    const [fieldConfig, setFieldConfig] = useState({
        rows: ['CB', '84', 'ST'],
        columns: ['Premier League', 'England', 'La Liga']
    })

    const generateBoardItems = () => {
        const rowArr = [];
        let columnArr = [];
        columnArr.push(<div style={{
            backgroundColor: '#076B00',
            width: '15vh',
            height: '15vh',
        }}>Fifa Grid</div>)
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