using System.Collections;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class VideoStream : MonoBehaviour
{
    public string streamUrl = "http://192.168.4.1:5000";
    public RawImage rawImage;

    void Start()
    {
        StartCoroutine(PlayStream());
    }

    IEnumerator PlayStream()
    {
        while (true)
        {
            UnityWebRequest www = UnityWebRequestTexture.GetTexture(streamUrl);
            yield return www.SendWebRequest();

            if (www.result != UnityWebRequest.Result.Success)
            {
                Debug.Log(www.error);
            }
            else
            {
                Texture2D texture = ((DownloadHandlerTexture)www.downloadHandler).texture;
                rawImage.texture = texture;
                rawImage.SetNativeSize();
            }
        }
    }
}