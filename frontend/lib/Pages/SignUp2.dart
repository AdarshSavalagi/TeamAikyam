import 'package:flutter/material.dart';

import '../Supportings/Signup.dart';
import '../Supportings/Signup2.dart';
import '../utils/constants.dart';

class SignUpScreen2 extends StatelessWidget {
  static String routeName = "/sign_up2";

  const SignUpScreen2({super.key, required this.name, required this.phone, required this.email, required this.password});
  final String name;
  final String phone;
  final String email;
  final String password;
  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: SafeArea(
        child: SizedBox(
          width: double.infinity,
          child: Padding(
            padding: EdgeInsets.symmetric(horizontal: 20),
            child: SingleChildScrollView(
              child: Column(
                children: [
                  SizedBox(height: 16),
                  Text("Financial Profile setup", style: headingStyle),
                  Text(
                    "Kickstart your financial journey \nwith our profile setup",
                    textAlign: TextAlign.center,
                  ),
                  SizedBox(height: 16),
                  SignUpForm2(),
                  SizedBox(height: 16),
                 
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
