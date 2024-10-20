import React from 'react';
import { View, Text, StyleSheet, Image, StyleProp, ViewStyle, TextStyle, ImageStyle } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';

interface CallItemProps {
  contactName: string;
  profilePicture: string;
  callType: 'incoming' | 'outgoing' | 'missed';
  date: string;
  containerStyle?: StyleProp<ViewStyle>;
  nameStyle?: StyleProp<TextStyle>;
  dateStyle?: StyleProp<TextStyle>;
  imageStyle?: StyleProp<ImageStyle>;
}

const CallItem: React.FC<CallItemProps> = ({
  contactName,
  profilePicture,
  callType,
  date,
  containerStyle,
  nameStyle,
  dateStyle,
  imageStyle,
}) => {
  const getIconName = (): string => {
    switch (callType) {
      case 'incoming':
        return 'call-received';
      case 'outgoing':
        return 'call-made';
      case 'missed':
        return 'call';
      default:
        return 'call';
    }
  };

  const iconName = getIconName();

  return (
    <View style={[styles.container, containerStyle]}>
      <Image source={{ uri: profilePicture }} style={[styles.image, imageStyle]} />
      <View style={styles.details}>
        <Text style={[styles.name, nameStyle]}>{contactName}</Text>
        <Text style={[styles.date, dateStyle]}>{date}</Text>
      </View>
      <Icon name={iconName} size={20} color="#5A2A83" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    padding: 15,
    backgroundColor: '#3A0078',
    borderRadius: 8,
    alignItems: 'center',
    marginVertical: 5,
  },
  image: {
    width: 50,
    height: 50,
    borderRadius: 25,
    borderWidth: 2,
    borderColor: '#5A2A83',
    marginRight: 15,
  },
  details: {
    flex: 1,
  },
  name: {
    fontSize: 16,
    color: '#fff',
    fontWeight: 'bold',
  },
  date: {
    fontSize: 12,
    color: '#ccc',
    marginTop: 2,
  },
});

export default CallItem;
