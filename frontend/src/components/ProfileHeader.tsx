import React from 'react';
import { View, Text, Image, StyleSheet, StyleProp, ViewStyle, TextStyle, ImageStyle } from 'react-native';

interface ProfileHeaderProps {
  name: string;
  profilePicture: string;
  containerStyle?: StyleProp<ViewStyle>;
  imageStyle?: StyleProp<ImageStyle>;
  nameStyle?: StyleProp<TextStyle>;
}

const ProfileHeader: React.FC<ProfileHeaderProps> = ({
  name,
  profilePicture,
  containerStyle,
  imageStyle,
  nameStyle,
}) => {
  return (
    <View style={[styles.container, containerStyle]}>
      <Image source={{ uri: profilePicture }} style={[styles.image, imageStyle]} />
      <Text style={[styles.name, nameStyle]}>{name}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#2E0854',
    borderBottomLeftRadius: 20,
    borderBottomRightRadius: 20,
    marginBottom: 20,
  },
  image: {
    width: 60,
    height: 60,
    borderRadius: 30,
    borderWidth: 2,
    borderColor: '#5A2A83',
    marginRight: 15,
  },
  name: {
    fontSize: 20,
    color: '#fff',
    fontWeight: 'bold',
  },
});

export default ProfileHeader;
