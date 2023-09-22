import React from "react"

export default function GridItem({row, column}) {


    return (
        <div style={{
            backgroundColor: 'rgb(50, 220, 50)',
            width: '15vh',
            height: '15vh',
            // border: 'solid 1px rgb(100, 100 ,100)'
        }}>
            {row}-{column}
        </div>
    )
}       