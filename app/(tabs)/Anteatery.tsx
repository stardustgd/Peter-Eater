import { StyleSheet } from 'react-native'

import MenuComponent from '@/components/MenuComponent'
import { Text, View } from '@/components/Themed'

export default function AnteateryTab() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>The Anteatery</Text>
      <View
        style={styles.separator}
        lightColor="#eee"
        darkColor="rgba(255,255,255,0.1)"
      />
      <MenuComponent />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
})