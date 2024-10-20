import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, FlatList } from 'react-native';
import Ionicons from 'react-native-vector-icons/Ionicons'; // Using react-native-vector-icons

const options = [
  { id: '1', icon: 'person-outline', title: 'Account' },
  { id: '2', icon: 'chatbox-outline', title: 'Chats' },
  { id: '3', icon: 'sunny-outline', title: 'Appearance' },
  { id: '4', icon: 'notifications-outline', title: 'Notification' },
  { id: '5', icon: 'shield-outline', title: 'Privacy' },
  { id: '6', icon: 'folder-outline', title: 'Data Usage' },
  { id: '7', icon: 'help-circle-outline', title: 'Help' },
  { id: '8', icon: 'mail-outline', title: 'Invite Your Friends' },
];

const SettingsScreen: React.FC = () => {
  return (
    <View style={styles.container}>
      {/* Profile Section */}
      <View style={styles.profileContainer}>
        <View style={styles.profileDetails}>
          <Ionicons name="person-circle-outline" size={40} color="#A0AABF" />
          <View style={{ marginLeft: 10 }}>
            <Text style={styles.profileName}>Almayra Zamzamy</Text>
            <Text style={styles.profileNumber}>+62 1309 - 1710 - 1920</Text>
          </View>
        </View>
        <Ionicons name="chevron-forward-outline" size={24} color="#A0AABF" />
      </View>

      {/* Options List */}
      <FlatList
        data={options}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <TouchableOpacity style={styles.optionItem}>
            <View style={styles.optionDetails}>
              <Ionicons name={item.icon} size={24} color="#A0AABF" />
              <Text style={styles.optionText}>{item.title}</Text>
            </View>
            <Ionicons name="chevron-forward-outline" size={24} color="#A0AABF" />
          </TouchableOpacity>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0E1624',
    padding: 15,
  },
  profileContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 15,
    borderBottomWidth: 1,
    borderBottomColor: '#1F2C40',
  },
  profileDetails: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  profileName: {
    fontSize: 18,
    color: '#FFFFFF',
    fontWeight: 'bold',
  },
  profileNumber: {
    fontSize: 14,
    color: '#A0AABF',
  },
  optionItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#1F2C40',
  },
  optionDetails: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  optionText: {
    fontSize: 16,
    color: '#FFFFFF',
    marginLeft: 15,
  },
});

export default SettingsScreen;
