import { Autocomplete, TextField } from '@mui/material'

export default function SearchBox() {


    o

    return (
        <>
            <Autocomplete 
                options={[]}
                renderInput={(params) => <TextField {...params} label="Player"/>}
            />

        </>
    )
}