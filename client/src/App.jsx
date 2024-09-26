import { Chat } from "./components";
import PageLayout from "./layout/PageLayout";
import { MessageProvider } from "./services/MessageContext";

function App() {
  return (
    <div className="min-h-screen">
      <MessageProvider>
        <PageLayout>
          <Chat />
        </PageLayout>
      </MessageProvider>
    </div>
  );
}

export default App;
