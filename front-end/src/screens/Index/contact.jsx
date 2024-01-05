import React, { useState } from "react";
import emailjs from "emailjs-com";

const initialState = {
  name: "",
  email: "",
  message: "",
};

export const Contact = (props) => {
  const [formData, setFormData] = useState(initialState);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const clearFormData = () => setFormData({ ...initialState });

  const handleSubmit = (e) => {
    e.preventDefault();

    emailjs
      .sendForm(
        "YOUR_SERVICE_ID",
        "YOUR_TEMPLATE_ID",
        e.target,
        "YOUR_USER_ID"
      )
      .then(
        (result) => {
          console.log(result.text);
          clearFormData();
        },
        (error) => {
          console.log(error.text);
        }
      );
  };

  return (
    <div>
    <div id="contact">
      <div className="container">
        <div className="row">
          <div className="col-md-12">
            <div className="section-title text-center">
              <h2>Get In Touch</h2>
              <p>
                Please fill out the form below to send us an email, and we
                will get back to you as soon as possible.
              </p>
            </div>
          </div>
        </div>
        <form name="sentMessage" validate onSubmit={handleSubmit}>
          <div className="row">
            <div className="col-md-6">
              <div className="form-group">
                <label htmlFor="name">Name</label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  className="form-control"
                  placeholder="Your Name"
                  required
                  value={formData.name}
                  onChange={handleChange}
                />
                <p className="help-block text-danger"></p>
              </div>
            </div>
            <div className="col-md-6">
              <div className="form-group">
                <label htmlFor="email">Email</label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  className="form-control"
                  placeholder="Your Email"
                  required
                  value={formData.email}
                  onChange={handleChange}
                />
                <p className="help-block text-danger"></p>
              </div>
            </div>
          </div>
          <div className="form-group">
            <label htmlFor="message">Message</label>
            <textarea
              name="message"
              id="message"
              className="form-control"
              rows="4"
              placeholder="Your Message"
              required
              value={formData.message}
              onChange={handleChange}
            ></textarea>
            <p className="help-block text-danger"></p>
          </div>
          <div id="success"></div>
          <button type="submit" className="btn btn-custom btn-lg">
            Send Message
          </button>
        </form>
      </div>
    </div>
    <div id="footer">
      <div className="container text-center">
        <p>
          &copy; 2023 Issaaf Kattan React Land Page Template. Design by{" "}
          <a href="http://www.templatewire.com" rel="nofollow">
            TemplateWire
          </a>
        </p>
      </div>
    </div>
  </div>
);
};