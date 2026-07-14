import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Settlement from "./pages/SettlementPredictor";
import Negotiation from "./pages/NegotiationEmail";
import Rights from "./pages/KnowYourRights";
import History from "./pages/History";

import Layout from "./components/Layout";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Login />} />

        <Route element={<Layout />}>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/settlement" element={<Settlement />} />
          <Route path="/negotiation" element={<Negotiation />} />
          <Route path="/rights" element={<Rights />} />
          <Route path="/history" element={<History />} />
        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;