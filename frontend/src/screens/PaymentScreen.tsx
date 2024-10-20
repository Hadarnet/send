import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import CustomButton from '../components/CustomButton';

const PaymentScreen = () => {
  const [inputValue, setInputValue] = useState('20000$');

  // Function to handle button press
  const handlePress = (value) => {
    setInputValue((prev) => prev + value);
  };

  // Function to delete last character
  const handleDelete = () => {
    setInputValue((prev) => prev.slice(0, -1)); // Remove the last character
  };

  return (
    <View style={styles.container}>
      <View style={styles.balanceContainer}>
        <Text style={styles.balanceText}>{inputValue}</Text>
      </View>
      <View style={styles.keypadContainer}>
        {['1', '2', '3', '4', '5', '6', '7', '8', '9', '#', '0'].map((key) => (
          <TouchableOpacity key={key} style={styles.keypadButton} onPress={() => handlePress(key)}>
            <Text style={styles.keypadText}>{key}</Text>
          </TouchableOpacity>
        ))}
        {/* Add a Delete button */}
        <TouchableOpacity style={styles.keypadButton} onPress={handleDelete}>
          <Text style={styles.keypadText}>DEL</Text>
        </TouchableOpacity>
      </View>
      <CustomButton
        title="Send Money"
        style={styles.sendButton}
        />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#101828',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  balanceContainer: {
    marginBottom: 30,
  },
  balanceText: {
    fontSize: 36,
    color: '#ffffff',
    fontWeight: 'bold',
  },
  keypadContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    width: '100%',
    justifyContent: 'space-between',
  },
  keypadButton: {
    width: '30%',
    backgroundColor: '#fff',
    padding: 20,
    justifyContent: 'center',
    alignItems: 'center',
    marginVertical: 10,
    borderRadius: 8,
  },
  keypadText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#000',
  },
  sendButton: {
    backgroundColor: '#1E63EE',
    paddingVertical: 20,
    paddingHorizontal: 100,
    borderRadius: 50,
    marginTop: 30,
  },
  sendButtonText: {
    color: '#ffffff',
    fontSize: 18,
    fontWeight: 'bold',
  },
});

export default PaymentScreen;
