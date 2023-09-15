import './App.css'
import TicTacToe from './pages/TicTacToe';
import { theme } from './theme';
import { ThemeProvider } from '@emotion/react';

function App() {

  return (
    <ThemeProvider theme={theme}>
      <>
        <TicTacToe/>
      </>
    </ThemeProvider>
  )
}

export default App
