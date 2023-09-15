export const apiServer = ' http://localhost:3000';


export const fetchAllPlayers = async () => {
    const response = await fetch(apiServer + '/general/all-players');
    if (!response.ok) throw Error('Could not fetch players');
    const result = await response.json();
    return result;
}