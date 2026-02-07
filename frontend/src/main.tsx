import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { App } from './App.tsx'
import { Home} from'./pages/Home.tsx'
import { ThemeProvider } from './components/theme-provider.tsx'
import { BrowserRouter, Routes, Route } from 'react-router'
import Form from './pages/Form.tsx'
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<App />} />
          <Route path='/home' element={<Home />} />
          <Route path='/Form' element={<Form/>}/>
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  </StrictMode>,
)
