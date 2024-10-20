import React, { createContext, useState, ReactNode, useEffect } from 'react';

// Define the shape of your context
interface AppContextProps {
  user: User | null;
  setUser: (user: User | null) => void;
  // Add other global states and setters as needed
}

// Define the User type
interface User {
  id: string;
  name: string;
  profilePicture: string;
  // Add other user properties
}

// Create the context with default values
export const AppContext = createContext<AppContextProps>({
  user: null,
  setUser: () => {},
});

// Create a provider component
export const AppProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);

  // Example: Fetch user data on mount
  useEffect(() => {
    // Replace with your actual user fetching logic
    const fetchUser = async () => {
      // Simulate fetching user data
      const fetchedUser: User = {
        id: '1',
        name: 'John Doe',
        profilePicture: 'https://example.com/profile.jpg',
      };
      setUser(fetchedUser);
    };

    fetchUser();
  }, []);

  return (
    <AppContext.Provider value={{ user, setUser }}>
      {children}
    </AppContext.Provider>
  );
};
