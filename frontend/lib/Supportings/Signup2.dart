import 'package:flutter/material.dart';

class SignUpForm2 extends StatefulWidget {
  const SignUpForm2({super.key});

  @override
  _SignUpFormState createState() => _SignUpFormState();
}

class _SignUpFormState extends State<SignUpForm2> {
  final _formKey = GlobalKey<FormState>();
  String? email;
  String? password;
  String? conform_password;
  String? Address;
  String? Name;
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
            keyboardType: TextInputType.number,
            onSaved: (newValue) => Name = newValue,
            onChanged: (value) {},
            controller: _controller[0],
            decoration: const InputDecoration(
              labelText: "Your Income",
              hintText: "Enter income",
              floatingLabelBehavior: FloatingLabelBehavior.always,
              suffixIcon: Icon(Icons.money),
            ),
          ),
          const SizedBox(
            height: 20,
          ),
          TextFormField(
            keyboardType: TextInputType.number,
            onSaved: (newValue) => Name = newValue,
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
         labelText: "Your Asset",
              hintText: "Enter Asset",
              floatingLabelBehavior: FloatingLabelBehavior.always,
              suffixIcon: Icon(Icons.money),
            ),
          ),
          const SizedBox(
            height: 20,
          ),

          TextFormField(
            keyboardType: TextInputType.number,
            onSaved: (newValue) => email = newValue,
            decoration: const InputDecoration(
              labelText: "loan",
              hintText: "Enter your loan",
              floatingLabelBehavior: FloatingLabelBehavior.always,
              // suffixIcon: CustomSurffixIcon(svgIcon: "assets/icons/Mail.svg"
              // ),
            ),
          ),
          // me
          const SizedBox(
            height: 20,
          ),
          TextFormField(
             keyboardType: TextInputType.text,
            onSaved: (newValue) => password = newValue,
            controller: _controller[5],
            onChanged: (value) {
              if (value.isNotEmpty) {
                // removeError(error: kPassNullError);
              } else if (value.length >= 8) {
                // removeError(error: kShortPassError);
              }
              password = value;
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
              labelText: "Financal goal",
              hintText: "Enter your Financal goal",
              floatingLabelBehavior: FloatingLabelBehavior.always,
              // suffixIcon: CustomSurffixIcon(svgIcon: "assets/icons/Lock.svg"),
            ),
          ),

          const SizedBox(height: 20),

          // FormError(errors: errors),
          const SizedBox(height: 20),
          ElevatedButton(
            onPressed: () {
             //submit form
            },
            child: const Text("Continue"),
          ),
        ],
      ),
    );
  }
}
