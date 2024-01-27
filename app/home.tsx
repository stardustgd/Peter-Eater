// import MenuComponent from '@/components/MenuComponent'
// import { Text } from '@/components/Themed'
// import FontAwesome from '@expo/vector-icons/FontAwesome'
// import { View, Pressable } from 'react-native'
// import { Link } from 'expo-router'
//
// import Colors from '@/constants/Colors'
// import { useColorScheme } from '@/components/useColorScheme'
//
// export default function Home() {
//   const colorScheme = useColorScheme()
//
//   return (
//     <View>
//       <Link href="/(tabs)/Brandywine" asChild>
//         <Pressable>
//           {({ pressed }) => (
//             <FontAwesome
//               name="info-circle"
//               size={25}
//               color={Colors[colorScheme ?? 'light'].text}
//               style={{
//                 marginRight: 15,
//                 opacity: pressed ? 0.5 : 1,
//               }}
//             />
//           )}
//         </Pressable>
//       </Link>
//     </View>
//   )
// }

import * as React from "react";
import { Image } from "expo-image";
import { StyleSheet, Text, View } from "react-native";
// import { Color, FontFamily } from "@/constants/Colors";

const PeterEaterOpeningPage = () => {
  return (
    <View style={styles.peterEaterOpeningPage}>
      <Image
        style={[styles.image14Icon, styles.iconPosition]}
        contentFit="cover"
      // source={require("../assets/peter_eater_home.png")}
      />
      <Image
        style={styles.plantforward0957Sz1Icon}
        contentFit="cover"
      // source={require("../assets/220121-plantforward-0957-sz-1.png")}
      />
      <Image
        style={styles.peterEaterHome1Icon}
        contentFit="cover"
        source={require("../assets/images/peter_eater_home.png")}
      />
      <Image
        style={[styles.image13Icon, styles.iconPosition]}
        contentFit="cover"
        source={require("../assets/images/filledonutproto.png")}
      />
      <Text style={styles.peterEater}>
        <Text style={styles.peter}>PETER</Text>
        <Text style={styles.text}>{` `}</Text>
        <Text style={styles.eater}>EATER</Text>
      </Text>
      <Image
        style={styles.maskGroupIcon}
        contentFit="cover"
      // source={require("../assets/mask-group.png")}
      />
      <Image
        style={styles.homebgwhiter1Icon}
        contentFit="cover"
      // source={require("../assets/homebgwhiter-1.png")}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  iconPosition: {
    display: "none",
    position: "absolute",
  },
  image14Icon: {
    top: -50,
    left: -62,
    width: 495,
    height: 978,
  },
  plantforward0957Sz1Icon: {
    top: -26,
    left: 0,
    width: 446,
    height: 1150,
    position: "absolute",
  },
  peterEaterHome1Icon: {
    top: -114,
    left: -104,
    width: 739,
    height: 1090,
    position: "absolute",
  },
  image13Icon: {
    top: 0,
    left: -5,
    width: 414,
    height: 896,
  },
  peter: {
    color: "#ffd200",
  },
  text: {
    color: "#000",
  },
  eater: {
    // color: Color.colorSteelblue,
    color: "#0064a4"
  },
  peterEater: {
    top: 433,
    left: 96,
    fontSize: 64,
    // fontFamily: FontFamily.odibeeSansRegular,
    fontFamily: "OdibeeSans-Regular",
    textAlign: "center",
    width: 231,
    height: 118,
    position: "absolute",
  },
  maskGroupIcon: {
    top: 241,
    left: 88,
    width: 212,
    height: 212,
    position: "absolute",
  },
  homebgwhiter1Icon: {
    top: -45,
    left: -83,
    width: 640,
    height: 943,
    position: "absolute",
  },
  peterEaterOpeningPage: {
    // backgroundColor: Color.colorWhite,
    backgroundColor: "#fff",
    flex: 1,
    width: "100%",
    height: 898,
    overflow: "hidden",
  },
});

export default PeterEaterOpeningPage;
