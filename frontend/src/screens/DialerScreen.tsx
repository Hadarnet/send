import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  SafeAreaView,
} from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons'; // Import the Ionicons

const DialerScreen = () => {
  const [phoneNumber, setPhoneNumber] = useState('');

  const handlePress = (value) => {
    setPhoneNumber(phoneNumber + value);
  };

  const handleDelete = () => {
    setPhoneNumber(phoneNumber.slice(0, -1));
  };

  const handleAddContact = () => {
    // Logic to add contact goes here
    alert('Add Contact functionality will be implemented.');
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        
        <Text style={styles.headerText}>Chats</Text>
        <TouchableOpacity onPress={handleAddContact} style={styles.addContactButton}>
          <Icon name="person-add" size={24} color="#ffffff" />
        </TouchableOpacity>
      </View>
      <View style={styles.numberDisplay}>
        <Text style={styles.phoneNumber}>{phoneNumber}</Text>
      </View>
      <View style={styles.dialPad}>
        {['1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '0', '#'].map((item, index) => (
          <TouchableOpacity
            key={index}
            style={styles.dialButton}
            onPress={() => handlePress(item)}
          >
            <Text style={styles.dialButtonText}>{item}</Text>
          </TouchableOpacity>
        ))}
      </View>
      <View style={styles.actionButtons}>
        <TouchableOpacity style={[styles.callButton, { backgroundColor: 'green' }]}>
          <Icon name="call" size={24} color="#ffffff" />
        </TouchableOpacity>
        <TouchableOpacity style={[styles.callButton, { backgroundColor: 'cyan' }]}>
          <Icon name="videocam" size={24} color="#ffffff" />
        </TouchableOpacity>
        <TouchableOpacity style={[styles.callButton, { backgroundColor: 'purple' }]} onPress={handleDelete}>
          <Icon name="backspace" size={24} color="#ffffff" />
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#101828',
    padding: 16,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingBottom: 20,
    justifyContent: 'space-between',
  },
  addContactButton: {
    marginRight: 10,
  },
  headerText: {
    color: '#ffffff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  numberDisplay: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: 20,
  },
  phoneNumber: {
    color: '#ffffff',
    fontSize: 28,
  },
  dialPad: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginTop: '20%',
  },
  dialButton: {
    backgroundColor: '#2C2F38',
    width: '30%',
    height: 100,
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 10,
    marginVertical: 10,
  },
  dialButtonText: {
    fontSize: 24,
    color: '#C39EFF',
  },
  actionButtons: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginTop: 20,
    
  },
  callButton: {
    width: '30%',
    height: 80,
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 10,
  },
  callButtonText: {
    color: '#ffffff',
    fontSize: 18,
  },
});

export default DialerScreen;
function alert(arg0: string) {
    throw new Error('Function not implemented.');
}

