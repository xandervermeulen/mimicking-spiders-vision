using System.Collections.Generic;
using System.Globalization;
using System.IO;
using UnityEngine;
using System;

public class MoveBall : MonoBehaviour
{

    public float frequencyX = 2f;
    public float frequencyY = 3f;
    public float frequencyZ = 1.5f; // Add a new frequency for Z coordinate

    public float amplitude = 2f;
    public float speed = 2f;

    private Vector3 _initialPosition;

    private string _filePath;

    private readonly DateTime currentDate = DateTime.Now;
    // Start is called before the first frame update

    void Start()
    {
        string fileName = "positions_xyz_" + currentDate.ToString("yyyy-MM-dd_HH'h'mm'm'") + ".csv";
        _filePath = Path.Combine(Application.dataPath, "Scripts/data/", fileName);
        _initialPosition = transform.position;
        CreateCsvFile();
    }

    // Update is called once per frame
    void Update()
    {
       float time = Time.time * speed;

        var x = _initialPosition.x + amplitude * Mathf.Sin(frequencyX * time);
        var y = _initialPosition.y + amplitude * Mathf.Sin(frequencyY * time);
        var z = _initialPosition.z + amplitude * Mathf.Sin(frequencyZ * time); 

        Vector3 newPosition = new Vector3(x, y, z);
        transform.position = newPosition;
        WriteXyzPosToCsv();
    }
    private void CreateCsvFile()
    {
        string[] headers = { "x", "y", "z" };
        string[] initialPositionArray = { _initialPosition.x.ToString(CultureInfo.InvariantCulture), _initialPosition.y.ToString(CultureInfo.InvariantCulture), _initialPosition.z.ToString(CultureInfo.InvariantCulture) };
        File.WriteAllLines(_filePath, new List<string[]> { headers, initialPositionArray }.ConvertAll(row => string.Join(",", row)));
        Debug.Log("CSV file created: positions_xyz.csv");
    }

    private void WriteXyzPosToCsv()
    {
        var transformPos = transform.position;
        string[] positions = { transformPos.x.ToString(CultureInfo.InvariantCulture), transformPos.y.ToString(CultureInfo.InvariantCulture), transformPos.z.ToString(CultureInfo.InvariantCulture) };
        File.AppendAllLines(_filePath, new List<string> { string.Join(",", positions) });
    }
}
