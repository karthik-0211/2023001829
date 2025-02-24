// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.3.1/firebase-app.js";
import { getDatabase,ref,set,get,child } from "https://www.gstatic.com/firebasejs/11.3.1/firebase-database.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyADqDiXmAh2NjH4a3a3wjmxwNF9Uq8hhS0",
  authDomain: "website-2f2e3.firebaseapp.com",
  projectId: "website-2f2e3",
  storageBucket: "website-2f2e3.firebasestorage.app",
  messagingSenderId: "898377961685",
  appId: "1:898377961685:web:f129fa90ffb70b22e5525c"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);