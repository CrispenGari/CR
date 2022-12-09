import * as mime from "react-native-mime-types";
export const generateRestImage = ({ uri, name }) => {
  const formData = new FormData();
  formData.append("image", {
    uri,
    name,
    filename: name,
    type: mime.lookup(uri) || "image/png",
  });
  formData.append("Content-Type", mime.lookup(uri) || "image/png");
  return formData;
};
