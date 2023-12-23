import { ThemeProvider } from "@/components/theme-provider"
import Hexon from './Hexon';




function App() {

  return (
      <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
        <Hexon />
      </ThemeProvider>
  )
}

export default App
