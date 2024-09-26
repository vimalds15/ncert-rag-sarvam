import React, { useState } from "react";
import { useMessageContext } from "../services/MessageContext";
import { sendAgentQuery, sendQuery } from "../api/message";
import LoaderSpinner from "./LoaderSpinner";

const Input = () => {
  const { addMessage } = useMessageContext();
  const [query, setQuery] = useState("");
  const [fetching, setFetching] = useState(false);
  const [selectedOption, setSelectedOption] = useState("default");

  const handleSelectChange = (event) => {
    setSelectedOption(event.target.value);
  };

  const handleAddMessage = async () => {
    setFetching(true);
    setQuery("");
    const userMessage = {
      type: "user",
      content: query,
    };
    addMessage(userMessage);
    let response;
    if (selectedOption === "default") {
      response = await sendQuery(query);
    } else {
      response = await sendAgentQuery(query);
    }
    console.log(response);
    const responseMessage = {
      type: "ai",
      content: response.data.response,
    };
    addMessage(responseMessage);
    setFetching(false);
  };

  return (
    <div className="flex items-center justify-center py-4 bg-red w-full">
      <div className="flex w-[90%] max-w-4xl border-2 border-zinc-400 pl-4 rounded-md overflow-hidden">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Type your query"
          disabled={fetching}
          className="w-full focus:outline-none pr-4 py-2"
        />
        {fetching ? (
          <LoaderSpinner />
        ) : (
          <input
            type="button"
            value="Send"
            disabled={fetching}
            onClick={handleAddMessage}
            className="font-semibold bg-black px-4 text-zinc-200 cursor-pointer"
          />
        )}
      </div>
      <div className="ml-2 border-zinc-400 border-2 py-2 px-2 text-sm">
        <select
          id="agent-select"
          value={selectedOption}
          onChange={handleSelectChange}
          className="w-20 focus:outline-none"
        >
          <option value="defaut">Default</option>
          <option value="agent">Agent</option>
        </select>
      </div>
    </div>
  );
};

export default Input;
