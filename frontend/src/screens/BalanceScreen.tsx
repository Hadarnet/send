// BalanceScreen.js with Victory Line Chart
import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, SafeAreaView } from 'react-native';
import { FlatList } from 'react-native-gesture-handler';
import { Image } from 'react-native-svg';
import { useNavigation } from '@react-navigation/native';
;

const BalanceScreen = () => {


  const navigation = useNavigation()

  const data = [
    { x: 'Jan', y: 45000 },
    { x: 'Feb', y: 47000 },
    { x: 'Mar', y: 43000 },
    { x: 'Apr', y: 48000 },
    { x: 'May', y: 47000 },
    { x: 'Jun', y: 47412 },
  ];

  const sendMoney = () => {
    navigation.navigate('PaymentScreen')
  }

  const mockTransactions = [
    { id: '1', name: 'Danny De Vito', date: '21.6.2021', amount: '482$', type: 'credit' },
    { id: '2', name: 'Danny De Vito', date: '21.6.2021', amount: '482$', type: 'debit' },
  ];

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.portfolioCard}>
        <Text style={styles.portfolioTitle}>Portfolio value</Text>
        <Text style={styles.portfolioValue}>$47,412.65</Text>
        <Text style={styles.portfolioChange}>$453.85 (+1.6%)</Text>
        
      </View>

      {/* Button Row */}
      <View style={styles.buttonRow}>
        <TouchableOpacity style={styles.button} onPress={sendMoney}>
          <Text style={styles.buttonText}>Send Money</Text>
        </TouchableOpacity>
        <TouchableOpacity style={[styles.button, styles.buttonMiddle]}>
          <Text style={styles.buttonText}>Ask for Money</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button}>
          <Text style={styles.buttonText}>Group</Text>
        </TouchableOpacity>
      </View>


      <FlatList
        data={mockTransactions}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.transactionItem}>
            <Image source={{ uri: 'https://via.placeholder.com/50' }} style={styles.profilePic} />
            <View style={styles.transactionDetails}>
              <Text style={styles.transactionName}>{item.name}</Text>
              <Text style={styles.transactionDate}>{item.date}</Text>
            </View>
            <Text style={styles.transactionAmount}>{item.amount}</Text>
            <Text style={[styles.transactionType, item.type === 'credit' ? styles.credit : styles.debit]}>
              {item.type === 'credit' ? '↑' : '↓'}
            </Text>
          </View>
        )}
      />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#101828',
    padding: 16,
  },
  portfolioCard: {
    backgroundColor: '#1E2630',
    borderRadius: 10,
    padding: 20,
    marginBottom: 20,
  },
  portfolioTitle: {
    color: '#B0B8C1',
    fontSize: 14,
  },
  portfolioValue: {
    color: '#ffffff',
    fontSize: 24,
    marginTop: 10,
  },
  portfolioChange: {
    color: '#0FA958',
    fontSize: 16,
    marginTop: 5,
  },
  buttonRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginVertical: 20,
  },
  button: {
    flex: 1,
    backgroundColor: '#1E2630',
    paddingVertical: 15,
    alignItems: 'center',
    borderRadius: 10,
    marginHorizontal: 5,
  },
  buttonMiddle: {
    backgroundColor: '#0FA958', // Green color for the middle button
  },
  buttonText: {
    color: '#ffffff',
    fontSize: 16,
  },
  transactionItem: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#2C2F38',
    borderRadius: 10,
    padding: 15,
    marginBottom: 10,
  },
  transactionDetails: {
    flex: 1,
  },
  transactionName: {
    color: '#ffffff',
    fontSize: 16,
  },
  transactionDate: {
    color: '#B0B8C1',
    fontSize: 14,
  },
  transactionAmount: {
    color: '#ffffff',
    fontSize: 18,
    marginRight: 10,
  },
  transactionType: {
    fontSize: 18,
  },
});

export default BalanceScreen;
