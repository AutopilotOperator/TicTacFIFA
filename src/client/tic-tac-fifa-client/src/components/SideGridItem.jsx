import { Grid } from "@mui/material";

export default function SideGridItem({value, isRow}) {


    return (
        <Grid item xs={4} style={{
            backgroundColor: 'rgb(50, 220, 50)',
            width: isRow? '10vh' : '15vh',
            height: '15vh',
            border: 'solid 1px rgb(100, 100 ,100)'
        }}>
            {value}
        </Grid>
    )
}