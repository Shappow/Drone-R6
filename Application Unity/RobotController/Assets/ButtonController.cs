using System;
using System.Collections;
using System.Collections.Generic;
using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class ButtonController : MonoBehaviour
{
    private TcpClient client;
    private NetworkStream stream;
    private string robotIPAddress;
    private int robotPort;
    private bool isCanon = false;
    private void Start()
    {
        try
        {
            client = new TcpClient(robotIPAddress, robotPort);
            stream = client.GetStream();
            string message = "B : " + isCanon.ToString();

            // Convertissez la chaîne de caractères en un tableau de bytes
            byte[] data = Encoding.ASCII.GetBytes(message);

            // Envoyez les données au robot
            stream.Write(data, 0, data.Length);
        }

        catch (Exception e)
        {
            // Gestion des erreurs lors de la connexion
            Debug.LogError("Erreur lors de la connexion au robot : " + e.Message);
            // Affichage d'un message d'erreur à l'utilisateur (facultatif)
            // UIManager.Instance.DisplayErrorMessage("Impossible de se connecter au robot !");
        }
    }

    public void SendButtonData ()  {

        if (isCanon) isCanon = false;
        else isCanon = true;
       
        string message = "B : " + isCanon.ToString() ;

        // Convertissez la chaîne de caractères en un tableau de bytes
        byte[] data = Encoding.ASCII.GetBytes(message);

        // Envoyez les données au robot
        stream.Write(data, 0, data.Length);
    }
    private void OnDestroy()
    {
        // Fermez la connexion lorsque le script est détruit
        stream.Close();
        client.Close();
    }
}
