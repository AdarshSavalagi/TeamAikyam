import 'package:flutter/material.dart';

import '../Pages/SignUp2.dart';

class SignUpForm extends StatefulWidget {
  const SignUpForm({super.key});

  @override
  _SignUpFormState createState() => _SignUpFormState();
}

class _SignUpFormState extends State<SignUpForm> {
  final _formKey = GlobalKey<FormState>();
  List<TextEditingController> _controller = [
    TextEditingController(),
    TextEditingController(),
    TextEditingController(),
    TextEditingController(),
    TextEditingController(),
    TextEditingController(),
  ];
  bool remember = false;
  final List<String?> errors = [];

  void addError({String? error}) {
    if (!errors.contains(error)) {
      setState(() {
        errors.add(error);
      });
    }
  }

  void removeError({String? error}) {
    if (errors.contains(error)) {
      setState(() {
        errors.remove(error);
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: [
          TextFormField(
            keyboardType: TextInputType.name,
            onChanged: (value) {},
            controller: _controller[0],
            decoration: const InputDecoration(
              labelText: "Name",
              hintText: "Name",
              floatingLabelBehavior: FloatingLabelBehavior.always,
              suffixIcon: Icon(Icons.person_2_outlined),
            ),
          ),
          const SizedBox(
            height: 20,
          ),
          TextFormField(
            keyboardType: TextInputType.phone,
            onChanged: (value) {},
            validator: (value) {
              if (value!.isEmpty) {
                // addError(error: kPhoneNumberNullError);
                return "";
              } else {
                return null;
              }
            },
            controller: _controller[1],
            decoration: const InputDecoration(
              labelText: "phone",
              hintText: "phone",
              floatingLabelBehavior: FloatingLabelBehavior.always,
              suffixIcon: Icon(Icons.phone),
            ),
          ),
          const SizedBox(
            height: 20,
          ),

          TextFormField(
            keyboardType: TextInputType.emailAddress,
            onChanged: (value) {},
            controller: _controller[2],
            validator: (value) {},
            decoration: const InputDecoration(
              labelText: "Email",
              hintText: "Enter your email",
              floatingLabelBehavior: FloatingLabelBehavior.always,
              // suffixIcon: CustomSurffixIcon(svgIcon: "assets/icons/Mail.svg"
              // ),
            ),
          ),
          // me
          const SizedBox(
            height: 20,
          ),

          const SizedBox(height: 20),
          TextFormField(
            obscureText: true,
            controller: _controller[3],
            onChanged: (value) {
              if (value.isNotEmpty) {
                // removeError(error: kPassNullError);
              } else if (value.length >= 8) {
                // removeError(error: kShortPassError);
              }
            },
            validator: (value) {
              if (value!.isEmpty) {
                // addError(error: kPassNullError);
                return "";
              } else if (value.length < 8) {
                // addError(error: kShortPassError);
                return "";
              }
              return null;
            },
            decoration: const InputDecoration(
              labelText: "Password",
              hintText: "Enter your password",
              floatingLabelBehavior: FloatingLabelBehavior.always,
              // suffixIcon: CustomSurffixIcon(svgIcon: "assets/icons/Lock.svg"),
            ),
          ),

          const SizedBox(height: 20),
          const SizedBox(height: 20),
          ElevatedButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => SignUpScreen2(name: _controller[0].text, phone: _controller[1].text, email: _controller[2].text, password: _controller[3].text,)),
              );
            },
            child: const Text("Continue"),
          ),
        ],
      ),
    );
  }
}
