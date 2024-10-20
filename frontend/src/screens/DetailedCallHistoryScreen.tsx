import React from 'react';
import { View, Text, FlatList, Image, StyleSheet } from 'react-native';

interface Call {
  id: string;
  type: string;
  date: string;
  duration: string;
}

const callHistory: Call[] = [
  { id: '1', type: 'Outgoing', date: 'Sept 12', duration: '5 min' },
  { id: '2', type: 'Missed', date: 'Sept 11', duration: '--' },
  { id: '3', type: 'Incoming', date: 'Sept 10', duration: '10 min' },
];

const DetailedCallHistoryScreen: React.FC = () => {
  return (
    <View style={styles.container}>
      <View style={styles.userInfo}>
        <Image 
          source={{ uri: 'https://user-profile-url.com/caller.jpg' }} 
          style={styles.profileImage} 
        />
        <Text style={styles.userName}>Samsung</Text>
      </View>

      <FlatList
        data={callHistory}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.callItem}>
            <Text>{item.type}</Text>
            <Text>{item.date}</Text>
            <Text>{item.duration}</Text>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFFFFF',
    padding: 10,
  },
  userInfo: {
    alignItems: 'center',
    marginBottom: 20,
  },
  profileImage: {
    width: 80,
    height: 80,
    borderRadius: 40,
  },
  userName: {
    fontSize: 20,
    fontWeight: 'bold',
    marginTop: 10,
  },
  callItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    padding: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#EEE',
  },
});

export default DetailedCallHistoryScreen;
