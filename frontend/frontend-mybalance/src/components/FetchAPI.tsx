import { useEffect } from "react";
import axios from "axios";

const useFetchData = (url: string) => {
  useEffect(() => {
    const fetchDataFromApi = async () => {
      try {
        const response = await axios.get(url);
        console.log(response.data);
      } catch (error) {
        console.error("An error occurred:", error);
      }
    };

    fetchDataFromApi(); // Call the function to initiate the data fetching.
  }, [url]); // Include 'url' in the dependency array if you want the effect to run whenever 'url' changes.
};

export default useFetchData;
