using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using UnityEngine.UI;

public class CameraController : MonoBehaviour
{
    public FixedJoystick translationJoystick;
    public FixedJoystick rotationJoystick;
    public Button canonToRotationButton;
    private int ButtonStatus;
    private TcpClient client;
    private NetworkStream stream;
    private string robotIPAddress;
    private int robotPort;
    private StreamReader reader;
    private Texture2D videoTexture;
    private Renderer videoRenderer;
    // Start is called before the first frame update
    void Start()
    {
        try
        {
            client = new TcpClient(robotIPAddress, robotPort);
            stream = client.GetStream();
        }
          
        catch (Exception e)
        {
            // Gestion des erreurs lors de la connexion
            Debug.LogError("Erreur lors de la connexion au robot : " + e.Message);
            // Affichage d'un message d'erreur à l'utilisateur (facultatif)
            // UIManager.Instance.DisplayErrorMessage("Impossible de se connecter au robot !");
        }
        videoTexture = new Texture2D(2, 2);
        videoRenderer = GetComponent<Renderer>();
        videoRenderer.material.mainTexture = videoTexture;
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        SendCoordinates();

        string videoData = reader.ReadLine();

    }

    private void SendCoordinates()
    {
        // Convertissez les coordonnées en une chaîne de caractères
        string message = "xT : " + (translationJoystick.Horizontal * 1000).ToString() + " yT : " + (translationJoystick.Vertical * 1000).ToString() + " xR : " + (translationJoystick.Horizontal * 1000).ToString() + " yR : " + (rotationJoystick.Vertical * 1000).ToString();

        // Convertissez la chaîne de caractères en un tableau de bytes
        byte[] data = Encoding.ASCII.GetBytes(message);

        // Envoyez les données au robot
        stream.Write(data, 0, data.Length);
    }

    private string GetVideoStream()
    {
        return reader.ReadLine();

    }
    private Texture2D DecodeVideoData(string videoData)
    {
        // Implémenter le décodage vidéo à partir des données reçues
        // Utiliser une bibliothèque de décodage vidéo comme FFmpeg ou des bibliothèques spécifiques à Unity
        // Retourner une texture Unity contenant l'image décodée
        // Exemple simplifié :
        return videoTexture;
    }
    private void OnDestroy()
    {
        // Fermez la connexion lorsque le script est détruit
        stream.Close();
        client.Close();
    }
}
