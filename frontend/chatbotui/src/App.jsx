// import React, { useState, useEffect, useRef } from 'react';
// import './App.css';

// const App = () => {
//   const [message, setMessage] = useState('');
//   const [chatHistory, setChatHistory] = useState([]);
//   const [isChatActive, setIsChatActive] = useState(true);
//   const [loading, setLoading] = useState(false);
//   const [conversationId, setConversationId] = useState(null);
//   const chatContainerRef = useRef(null);


//   useEffect(() => {
//     if (chatContainerRef.current) {
//       chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
//     }
//   }, [chatHistory]);

//   useEffect(() => {
//     if (!conversationId) {
//       setConversationId(Date.now().toString());
//     }
//   }, [conversationId]);

//   const sendMessage = async (event) => {
//     event.preventDefault();

//     if (message.trim() === '') return;

//     setLoading(true);
//     setChatHistory((prevHistory) => [
//       ...prevHistory,
//       { sender: 'user', text: message },
//     ]);

//     try {
//       const response = await fetch(`http://localhost:8000/chat/`, {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({
//           message,
//           conversation_id: conversationId, // Send the conversation_id with the message
//         }),
//       });

//       if (!response.ok) {
//         throw new Error('Error with API request');
//       }

//       const data = await response.json();
//       setChatHistory((prevHistory) => [
//         ...prevHistory,
//         { sender: 'ai', text: data.response },
//       ]);
//       setMessage('');
//     } catch (error) {
//       console.error('Error:', error);
//       setLoading(false);
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="bg-zinc-950 fixed inset-0 flex justify-center items-center p-4">

//       <div className="w-full max-w-lg bg-zinc-900 rounded-lg shadow-lg p-4 sm:p-6">
//         <div className="flex justify-between items-center mb-4">
//           <h1 className="text-xl text-white sm:text-2xl font-semibold">PaulBot</h1>
//         </div>

//         <div
//           ref={chatContainerRef}
//           className="overflow-y-auto h-96 space-y-4 mb-4 p-4 border border-zinc-900 rounded-lg "
//         >
//           {chatHistory.map((msg, index) => (
//             <div
//               key={index}
//               className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}
//             >
//               <div className={`max-w-xs p-3 rounded-lg ${msg.sender === 'user' ? 'bg-blue-600 text-white' : 'bg-zinc-700 text-white'}`}>
//                 {msg.text}
//               </div>
//             </div>
//           ))}

//           {loading && (
//             <div className="flex justify-start">
//               <div className="max-w-xs p-3 rounded-lg bg-gray-900 text-white animate-pulse">
//                 AI is typing...
//               </div>
//             </div>
//           )}
//         </div>


//         {isChatActive && (
//           <form onSubmit={sendMessage} className="flex flex-col sm:flex-row items-center  sm:space-x-2">
//             <input
//               type="text"
//               value={message}
//               onChange={(e) => setMessage(e.target.value)}
//               className="w-full p-2 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-zinc-950 text-white text-sm sm:text-base"
//               placeholder="Type your message..."
//             />
//             <button
//               type="submit"
//               className="bg-gray-600 text-white py-2 px-4 rounded-lg text-sm sm:text-base disabled:opacity-50"
//               disabled={loading || !message.trim()}
//             >
//               Send
//             </button>
//           </form>
//         )}
//       </div>
//     </div>
//   );
// };

// export default App;







// import React, { useState, useEffect, useRef } from 'react';
// import './App.css';

// const App = () => {
//   const [message, setMessage] = useState('');
//   const [chatHistory, setChatHistory] = useState([]);
//   const [isChatActive, setIsChatActive] = useState(true);
//   const [loading, setLoading] = useState(false);
//   const [conversationId, setConversationId] = useState(null);
//   const chatContainerRef = useRef(null);

//   useEffect(() => {
//     if (chatContainerRef.current) {
//       chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
//     }
//   }, [chatHistory]);

//   useEffect(() => {
//     if (!conversationId) {
//       setConversationId(Date.now().toString());
//     }
//   }, [conversationId]);

//   const sendMessage = async (event) => {
//     event.preventDefault();

//     if (message.trim() === '') return;

//     setLoading(true);
//     setChatHistory((prevHistory) => [
//       ...prevHistory,
//       { sender: 'user', text: message },
//     ]);

//     try {
//       const response = await fetch(`http://localhost:8000/chat/`, {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({
//           message,
//           conversation_id: conversationId,
//         }),
//       });

//       if (!response.ok) {
//         throw new Error('Error with API request');
//       }

//       const data = await response.json();
//       setChatHistory((prevHistory) => [
//         ...prevHistory,
//         { sender: 'ai', text: data.response },
//       ]);
//       setMessage('');
//     } catch (error) {
//       console.error('Error:', error);
//       setLoading(false);
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     // <div className="bg-gradient-to-br from-purple-900 via-gray-950 to-black min-h-screen flex items-center justify-center p-6">
//     //   <div className="w-full max-w-3xl bg-opacity-90 bg-zinc-900 rounded-3xl shadow-2xl border border-zinc-800 p-6 sm:p-8 backdrop-blur-md">
//     //     <div className="flex items-center justify-between mb-6">
//     //       <h1 className="text-4xl sm:text-5xl font-extrabold text-white tracking-widest animate-fade-in drop-shadow-md">PaulBot 🤖</h1>
//     //       {/* <span className="text-sm text-gray-400 italic animate-fade-in delay-100">Powered by Groq & FastAPI</span> */}
//     //     </div>

//     <div className="bg-gradient-to-br from-purple-900 via-gray-950 to-black min-h-screen flex items-center justify-center p-6">
//       {/* <div className="w-full max-w-[650px] h-[900px] bg-opacity-90 bg-zinc-900 rounded-3xl shadow-2xl border border-zinc-800 p-6 sm:p-8 backdrop-blur-md flex flex-col"> */}
//       <div className="w-full max-w-[650px] h-[800px] bg-opacity-90 bg-zinc-900 rounded-3xl shadow-2xl border border-zinc-800 p-6 sm:p-8 backdrop-blur-md flex flex-col">
//         <div className="flex items-center justify-between mb-6">
//           <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-widest animate-fade-in drop-shadow-md">
//             PaulBot 🤖
//           </h1>
//         </div>

//         <div
//           ref={chatContainerRef}
//           className="overflow-y-auto h-[32rem] bg-gradient-to-br from-zinc-800 to-zinc-900 rounded-xl p-5 space-y-6 border border-zinc-700 shadow-inner scrollbar-thin scrollbar-thumb-zinc-700 scrollbar-track-transparent"
//         >
//           {chatHistory.map((msg, index) => (
//             <div
//               key={index}
//               className={`w-full flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'} animate-fade-up`}
//             >
//               {/* <div className={`relative mr-[20px] ml-[20px] group max-w-[75%] px-6 py-4 rounded-3xl text-base sm:text-lg shadow-lg border transition-all duration-300 transform hover:scale-[1.03] backdrop-blur-md ${msg.sender === 'user' ? 'bg-gradient-to-r from-blue-700 to-blue-500 text-white border-blue-300' : 'bg-gradient-to-r from-gray-700 to-zinc-700 text-white border-zinc-500'}`}> */}
//               {/* <div className={`relative mr-[20px] ml-[20px] group max-w-[75%] px-6 py-4 rounded-3xl text-lg sm:text-xl shadow-lg border transition-all duration-300 transform hover:scale-[1.03] backdrop-blur-md ${msg.sender === 'user' ? 'bg-gradient-to-r from-blue-700 to-blue-500 text-white border-blue-300' : 'bg-gradient-to-r from-gray-700 to-zinc-700 text-white border-zinc-500'}`}> */}
//               <div className={`relative mr-[20px] ml-[20px] group max-w-[75%] px-6 py-4 rounded-3xl text-[24px] sm:text-[28px] shadow-lg border transition-all duration-300 transform hover:scale-[1.03] backdrop-blur-md ${msg.sender === 'user' ? 'bg-gradient-to-r from-blue-700 to-blue-500 text-white border-blue-300' : 'bg-gradient-to-r from-gray-700 to-zinc-700 text-white border-zinc-500'}`}>
//               {/* <div className={`relative mr-[20px] ml-[20px] group max-w-[75%] px-6 py-4 rounded-3xl text-[24px] sm:text-[28px] shadow-lg border transition-all duration-300 transform hover:scale-[1.03] backdrop-blur-md ${msg.sender === 'user' ? 'bg-gradient-to-r from-purple-600 to-pink-500 text-white border-pink-300' : 'bg-gradient-to-r from-gray-800 to-slate-700 text-white border-slate-600'}`}> */}

//                 <p>{msg.text}</p>
//                 <span className="absolute -bottom-3 right-4 text-xs text-gray-400 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
//                   {msg.sender === 'user' ? 'You' : 'PaulBot'}
//                 </span>
//               </div>
//             </div>
//           ))}

//           {loading && (
//             <div className="flex justify-start animate-pulse">
//               <div className="max-w-xs px-4 py-2 rounded-xl bg-gray-900 text-white shadow-md">
//                 AI is typing...
//               </div>
//             </div>
//           )}
//         </div>

//         {isChatActive && (
//           <form
//             onSubmit={sendMessage}
//             className="mt-8 flex flex-col sm:flex-row items-center gap-4 animate-fade-in"
//           >
//             <input
//               type="text"
//               value={message}
//               onChange={(e) => setMessage(e.target.value)}
//               className="flex-grow mt-[10px] mb-[10px] px-5 py-3 rounded-2xl bg-zinc-950 border border-zinc-700 focus:outline-none focus:ring-2 focus:ring-blue-500 text-white text-base placeholder-gray-500 shadow-inner"
//               placeholder="Ask something..."
//             />

//             <button
//               type="submit"
//               className="bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-700 hover:to-blue-600 text-white font-bold text-2xl py-6 px-12 rounded-3xl shadow-lg transition duration-300 ease-in-out disabled:opacity-50"
//               disabled={loading || !message.trim()}
//             >
//               Send
//             </button>



//             {/* <button
//               type="submit"
//               className="bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-700 hover:to-blue-600 text-white font-semibold py-2 px-6 rounded-2xl shadow-md transition duration-300 ease-in-out disabled:opacity-50"
//               disabled={loading || !message.trim()}
//             >
//               Send
//             </button> */}
//           </form>
//         )}
//       </div>
//     </div>
//   );
// };

// export default App;







// import React, { useState, useEffect, useRef } from 'react';
// import './App.css';

// const App = () => {
//   const [message, setMessage] = useState('');
//   const [chatHistory, setChatHistory] = useState([]);
//   const [isChatActive, setIsChatActive] = useState(true);
//   const [loading, setLoading] = useState(false);
//   const [conversationId, setConversationId] = useState(null);
//   const chatContainerRef = useRef(null);

//   useEffect(() => {
//     if (chatContainerRef.current) {
//       chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
//     }
//   }, [chatHistory]);

//   useEffect(() => {
//     if (!conversationId) {
//       setConversationId(Date.now().toString());
//     }
//   }, [conversationId]);

//   const sendMessage = async (event) => {
//     event.preventDefault();
//     if (message.trim() === '') return;

//     setLoading(true);
//     setChatHistory((prevHistory) => [
//       ...prevHistory,
//       { sender: 'user', text: message },
//     ]);

//     try {
//       const response = await fetch(`http://localhost:8000/chat/`, {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ message, conversation_id: conversationId }),
//       });

//       if (!response.ok) throw new Error('Error with API request');

//       const data = await response.json();
//       setChatHistory((prevHistory) => [
//         ...prevHistory,
//         { sender: 'ai', text: data.response },
//       ]);
//       setMessage('');
//     } catch (error) {
//       console.error('Error:', error);
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="bg-gradient-to-br from-purple-900 via-gray-950 to-black min-h-screen flex items-center justify-center p-6">
//       <div className="w-full max-w-[650px] h-[800px] bg-opacity-90 bg-zinc-900 rounded-3xl shadow-2xl border border-zinc-800 p-6 sm:p-8 backdrop-blur-md flex flex-col">
//         <div className="flex items-center justify-between mb-6">
//           <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-widest animate-fade-in drop-shadow-md">
//             PaulBot 🤖
//           </h1>
//         </div>

//         <div
//           ref={chatContainerRef}
//           className="overflow-y-auto h-[32rem] bg-gradient-to-br from-zinc-800 to-zinc-900 rounded-xl p-5 space-y-6 border border-zinc-700 shadow-inner scrollbar-thin scrollbar-thumb-zinc-700 scrollbar-track-transparent"
//         >
//           {chatHistory.map((msg, index) => (
//             <div
//               key={index}
//               className={`w-full flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'} animate-fade-up`}
//             >
//               <div className={`relative mr-[20px] ml-[20px] group max-w-[75%] px-6 py-4 rounded-3xl text-[20px] sm:text-[22px] shadow-lg border transition-all duration-300 transform hover:scale-[1.03] backdrop-blur-md ${msg.sender === 'user'
//                 ? 'bg-gradient-to-r from-blue-700 to-blue-500 text-white border-blue-300'
//                 : 'bg-gradient-to-r from-gray-700 to-zinc-700 text-white border-zinc-500'
//                 }`}>
//                 <p>{msg.text}</p>
//                 <span className="absolute -bottom-3 right-4 text-xs text-gray-400 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
//                   {msg.sender === 'user' ? 'You' : 'PaulBot'}
//                 </span>
//               </div>
//             </div>
//           ))}

//           {loading && (
//             <div className="flex justify-start animate-pulse">
//               <div className="max-w-xs px-4 py-2 rounded-xl bg-gray-900 text-white shadow-md">
//                 AI is typing...
//               </div>
//             </div>
//           )}
//         </div>

//         {isChatActive && (
//           <form
//             onSubmit={sendMessage}
//             className="mt-6 flex flex-row items-center gap-4 animate-fade-in"
//           >
//             <input
//               type="text"
//               value={message}
//               onChange={(e) => setMessage(e.target.value)}
//               className="flex-grow px-5 py-3 rounded-2xl bg-zinc-950 border border-zinc-700 focus:outline-none focus:ring-2 focus:ring-blue-500 text-white text-base placeholder-gray-500 shadow-inner"
//               placeholder="Ask something..."
//             />

//             <button
//               type="submit"
//               disabled={loading || !message.trim()}
//               className="focus:outline-none"
//             >
//               <img
//                 src="/img.png"
//                 alt="Send"
//                 className="w-1 h-1 object-contain rounded-lg hover:scale-105 transition-transform duration-200"
//                 style={{ maxWidth: '60px', maxHeight: '60px', padding: '0', margin: '0', border: 'none', boxShadow: 'none', outline: 'none', background: 'transparent' }}
//               />
//             </button>
//           </form>
//         )}
//       </div>
//     </div>
//   );
// };

// export default App;










// import React, { useState, useEffect, useRef } from 'react';
// import './App.css';

// const App = () => {
//   const [message, setMessage] = useState('');
//   const [chatHistory, setChatHistory] = useState([]);
//   const [isChatActive, setIsChatActive] = useState(true);
//   const [loading, setLoading] = useState(false);
//   const [conversationId, setConversationId] = useState(null);
//   const chatContainerRef = useRef(null);

//   useEffect(() => {
//     if (chatContainerRef.current) {
//       chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
//     }
//   }, [chatHistory]);

//   useEffect(() => {
//     if (!conversationId) {
//       setConversationId(Date.now().toString());
//     }
//   }, [conversationId]);

//   const sendMessage = async (event) => {
//     event.preventDefault();
//     if (message.trim() === '') return;

//     setLoading(true);
//     setChatHistory((prevHistory) => [
//       ...prevHistory,
//       { sender: 'user', text: message },
//     ]);

//     try {
//       const response = await fetch(`http://localhost:8000/chat/`, {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ message, conversation_id: conversationId }),
//       });

//       if (!response.ok) throw new Error('Error with API request');

//       const data = await response.json();
//       setChatHistory((prevHistory) => [
//         ...prevHistory,
//         { sender: 'ai', text: data.response },
//       ]);
//       setMessage('');
//     } catch (error) {
//       console.error('Error:', error);
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="bg-gradient-to-br from-purple-900 via-gray-950 to-black min-h-screen flex items-center justify-center p-6">
//       <div className="w-full max-w-[650px] h-[800px] bg-opacity-90 bg-zinc-900 rounded-3xl shadow-2xl border border-zinc-800 p-6 sm:p-8 backdrop-blur-md flex flex-col">
//         <div className="flex items-center justify-between mb-6">
//           <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-widest animate-fade-in drop-shadow-md">
//             PaulBot 🤖
//           </h1>
//         </div>

//         <div
//           ref={chatContainerRef}
//           className="overflow-y-auto h-[32rem] bg-gradient-to-br from-zinc-800 to-zinc-900 rounded-xl p-5 space-y-6 border border-zinc-700 shadow-inner scrollbar-thin scrollbar-thumb-zinc-700 scrollbar-track-transparent"
//         >
//           {chatHistory.map((msg, index) => (
//             <div
//               key={index}
//               className={`w-full flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'} animate-fade-up`}
//             >
//               <div
//                 className={`relative group max-w-[75%] text-[20px] sm:text-[22px] transition-all duration-300 transform hover:scale-[1.03] ${msg.sender === 'user'
//                   ? 'bg-gradient-to-r from-blue-700 to-blue-500 text-white border-blue-300'
//                   : 'bg-gradient-to-r from-gray-700 to-zinc-700 text-white border-zinc-500'
//                   }`}
//                 style={{
//                   borderRadius: '24px',
//                   boxShadow: '0 4px 12px rgba(0, 0, 0, 0.3)',
//                   border: '1.5px solid',
//                   padding: '16px 20px',
//                   marginLeft: '20px',
//                   marginRight: '20px',
//                   backdropFilter: 'blur(4px)',
//                 }}
//               >
//                 <p>{msg.text}</p>
//                 <span className="absolute -bottom-3 right-4 text-xs text-gray-400 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
//                   {msg.sender === 'user' ? 'You' : 'PaulBot'}
//                 </span>
//               </div>
//             </div>
//           ))}

//           {loading && (
//             <div className="flex justify-start animate-pulse">
//               <div className="max-w-xs px-4 py-2 rounded-xl bg-gray-900 text-white shadow-md">
//                 AI is typing...
//               </div>
//             </div>
//           )}
//         </div>

//         {isChatActive && (
//           <form
//             onSubmit={sendMessage}
//             className="mt-6 flex flex-row items-center gap-4 animate-fade-in"
//           >
//             <input
//               type="text"
//               value={message}
//               onChange={(e) => setMessage(e.target.value)}
//               className="flex-grow px-5 py-3 rounded-2xl bg-zinc-950 border border-zinc-700 focus:outline-none focus:ring-2 focus:ring-blue-500 text-white text-base placeholder-gray-500 shadow-inner"
//               placeholder="Ask something..."
//             />

//             <button
//               type="submit"
//               disabled={loading || !message.trim()}
//               className="focus:outline-none"
//             >
//               <img
//                 src="/img.png"
//                 alt="Send"
//                 className="object-contain rounded-md hover:scale-105 transition-transform duration-200"
//                 style={{
//                   width: '36px',
//                   height: '36px',
//                   border: 'none',
//                   padding: '0',
//                   margin: '0',
//                   background: 'transparent',
//                 }}
//               />
//             </button>
//           </form>
//         )}
//       </div>
//     </div>
//   );
// };

// export default App;






// import React, { useState, useEffect, useRef } from 'react';
// import './App.css';

// const App = () => {
//   const [message, setMessage] = useState('');
//   const [chatHistory, setChatHistory] = useState([]);
//   const [isChatActive, setIsChatActive] = useState(true);
//   const [loading, setLoading] = useState(false);
//   const [conversationId, setConversationId] = useState(null);
//   const chatContainerRef = useRef(null);

//   useEffect(() => {
//     if (chatContainerRef.current) {
//       chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
//     }
//   }, [chatHistory]);

//   useEffect(() => {
//     if (!conversationId) {
//       setConversationId(Date.now().toString());
//     }
//   }, [conversationId]);

//   const sendMessage = async (event) => {
//     event.preventDefault();
//     if (message.trim() === '') return;

//     setLoading(true);
//     setChatHistory((prevHistory) => [
//       ...prevHistory,
//       { sender: 'user', text: message },
//     ]);

//     try {
//       const response = await fetch(`http://localhost:8000/chat/`, {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ message, conversation_id: conversationId }),
//       });

//       if (!response.ok) throw new Error('Error with API request');

//       const data = await response.json();
//       setChatHistory((prevHistory) => [
//         ...prevHistory,
//         { sender: 'ai', text: data.response },
//       ]);
//       setMessage('');
//     } catch (error) {
//       console.error('Error:', error);
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="bg-gradient-to-br from-purple-900 via-gray-950 to-black min-h-screen flex items-center justify-center p-6">
//       <div className="w-full max-w-[700px] h-[800px] bg-opacity-90 bg-zinc-900 rounded-3xl shadow-2xl border border-zinc-800 p-6 sm:p-8 backdrop-blur-md flex flex-col">
//         <div className="flex items-center justify-between mb-6">
//           <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-widest animate-fade-in drop-shadow-md">
//             PaulBot 🤖
//           </h1>
//         </div>

//         <div
//           ref={chatContainerRef}
//           className="overflow-y-auto h-[32rem] bg-gradient-to-br from-zinc-800 to-zinc-900 rounded-xl p-5 space-y-6 border border-zinc-700 shadow-inner scrollbar-thin scrollbar-thumb-zinc-700 scrollbar-track-transparent"
//         >
//           {chatHistory.map((msg, index) => (
//             <div
//               key={index}
//               className={`w-full flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'} animate-fade-up`}
//             >
//               <div className={`${msg.sender === 'user' ? 'user-message' : 'ai-message'} chat-bubble`}>
//                 <p>{msg.text}</p>
//                 <span className="absolute -bottom-3 right-4 text-xs mr=[10px] text-gray-400 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
//                   {msg.sender === 'user' ? 'You' : 'PaulBot'}
//                 </span>
//               </div>
//             </div>
//           ))}

//           {loading && (
//             <div className="flex justify-start animate-pulse">
//               <div className="max-w-xs px-4 py-2 rounded-xl bg-gray-900 text-white shadow-md">
//                 AI is typing...
//               </div>
//             </div>
//           )}
//         </div>

//         {isChatActive && (
//           <form
//             onSubmit={sendMessage}
//             className="mt-6 flex flex-row items-center gap-4 animate-fade-in"
//           >
//             <input
//               type="text"
//               value={message}
//               onChange={(e) => setMessage(e.target.value)}
//               className="flex-grow px-5 py-3 rounded-2xl bg-zinc-950 border border-zinc-700 focus:outline-none focus:ring-2 focus:ring-blue-500 text-white text-base placeholder-gray-500 shadow-inner"
//               placeholder="Ask something..."
//             />

//             <button
//               type="submit"
//               disabled={loading || !message.trim()}
//               className="focus:outline-none"
//             >
//               <img
//                 src="/img.png"
//                 alt="Send"
//                 className="w-[40px] h-[40px] object-contain rounded-lg hover:scale-105 transition-transform duration-200"
//                 style={{
//                   border: 'none',
//                   boxShadow: 'none',
//                   outline: 'none',
//                   background: 'transparent',
//                 }}
//               />
//             </button>
//           </form>
//         )}
//       </div>
//     </div>
//   );
// };

// export default App;






import React, { useState, useEffect, useRef } from 'react';
import './App.css';

const App = () => {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [isChatActive, setIsChatActive] = useState(true);
  const [loading, setLoading] = useState(false);
  const [conversationId, setConversationId] = useState(null);
  const chatContainerRef = useRef(null);

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }
  }, [chatHistory]);

  useEffect(() => {
    if (!conversationId) {
      setConversationId(Date.now().toString());
    }
  }, [conversationId]);

  const sendMessage = async (event) => {
    event.preventDefault();
    if (message.trim() === '') return;

    setLoading(true);
    setChatHistory((prevHistory) => [
      ...prevHistory,
      { sender: 'user', text: message },
    ]);

    try {
      const response = await fetch(`http://localhost:8000/chat/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message, conversation_id: conversationId }),
      });

      if (!response.ok) throw new Error('Error with API request');

      const data = await response.json();
      setChatHistory((prevHistory) => [
        ...prevHistory,
        { sender: 'ai', text: data.response },
      ]);
      setMessage('');
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-gradient-to-br from-purple-900 via-gray-950 to-black min-h-screen flex items-center justify-center py-10 px-4">
      <div className="w-full max-w-[650px] max-h-[95vh] bg-opacity-90 bg-zinc-900 rounded-3xl shadow-2xl border border-zinc-800 p-6 sm:p-8 backdrop-blur-md flex flex-col">
        <div className="flex items-center justify-between mb-6">
          <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-widest animate-fade-in drop-shadow-md ml-[10px]">
            PaulBot 🤖
          </h1>
        </div>

        <div
          ref={chatContainerRef}
          className="overflow-y-auto flex-grow bg-gradient-to-br from-zinc-800 to-zinc-900 rounded-xl p-5 space-y-6 border border-zinc-700 shadow-inner scrollbar-thin scrollbar-thumb-zinc-700 scrollbar-track-transparent"
        >
          {chatHistory.map((msg, index) => (
            <div
              key={index}
              className={`w-full flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'} animate-fade-up`}
            >
              <div className={`${msg.sender === 'user' ? 'user-message' : 'ai-message'} chat-bubble`}>
                <p>{msg.text}</p>
              </div>
            </div>
          ))}

          {loading && (
            <div className="flex justify-start animate-pulse">
              <div className="max-w-xs px-4 py-2 rounded-xl bg-gray-900 text-white shadow-md">
                AI is typing...
              </div>
            </div>
          )}
        </div>

        {isChatActive && (
          <form
            onSubmit={sendMessage}
            className="mt-4 flex flex-row items-center gap-4 animate-fade-in"
          >
            <input
              type="text"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              className="flex-grow px-10 py-10 rounded-2xl bg-zinc-950 border border-zinc-700 focus:outline-none focus:ring-2 focus:ring-blue-500 text-white text-xl placeholder-gray-400 shadow-inner"
              // className="flex-grow px-10 py-7 rounded-2xl bg-zinc-950 border border-zinc-700 focus:outline-none focus:ring-2 focus:ring-blue-500 text-white text-base placeholder-gray-500 shadow-inner"
              placeholder="Ask something..."
            />

            <button
              type="submit"
              disabled={loading || !message.trim()}
              className="focus:outline-none"
            >
              <img
                src="/img.png"
                alt="Send"
                className="w-[50px] h-[55px] object-contain hover:scale-105 transition-transform duration-200"
                style={{
                  border: 'none',
                  background: 'transparent',
                  padding: 0,
                  margin: 0,
                  boxShadow: 'none',
                }}
              />
            </button>
          </form>
        )}
      </div>
    </div>
  );
};

export default App;
